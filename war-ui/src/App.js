import './App.css';
import React, {Component} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css';


const BACKEND_URL = 'http://' + process.env.REACT_APP_BACKEND_IP + ':4000';
console.log(BACKEND_URL)

export default class App extends Component {

  constructor(props) {
      super(props);
      this.state = {
          players: [],
          player1:'',
          player2:'',
          gameMessage:'',
          gameLogs:[],  
          logsShown:0,
          result: -1,
          selectedPlayer:'',
          selectedPlayerWins: '',
          isPlayerSelected: 0, 
          newUser: '',
          newUserMessage: '',
          allPlayersWins: [],
          init: 1
      }
  }

  refreshUsers(){
    axios.get(BACKEND_URL+'/users')
      .then(response => {
          this.setState({players: response.data});
          console.log(response.data);
          if (response.data.length > 0){
            console.log(response.data[0].name)
            if(this.state.init > 0){
              this.setState({
                player1: response.data[0].name,
                player2: response.data[0].name,
                init: 0
              })
              console.log("initing");
            }
            this.getPlayerWinsUtil(response.data[0].name)
          }
        })
      .catch(function(error) {
          console.log(error);
      })

    axios.get(BACKEND_URL+'/wins/users')
    .then(response => {
      this.setState({
        allPlayersWins: response.data
      })
    })
  }

  componentDidMount(){
    console.log(process.env.NODE_ENV);
    this.refreshUsers()
  }

  getPlayerWins = (e) => {
    console.log("herer1");
    this.getPlayerWinsUtil(e.target.value);
  };

  getPlayerWinsUtil (p_name){
    this.setState({selectedPlayer : p_name, isPlayerSelected: 1});
    axios.get(BACKEND_URL+'/wins/users/'+p_name)
      .then(response => {
        this.setState({
          selectedPlayerWins: response.data.wins.toString()
        })
      })
      .catch(function(error) {
        console.log(error);
    })
  }

  setPlayer1 = (e) => {
    console.log(this.state.player1)
    console.log(e.target.value)
    this.setState({player1 : e.target.value, result:-1, gameMessage:'', logsShown: 0});
  };

  setPlayer2 = (e) => {
    console.log(this.state.player2)
    console.log(e.target.value)
    this.setState({player2 : e.target.value, result:-1, gameMessage:'', logsShown: 0});
    console.log("2")
  };

  playGame = (e) => {
    const send = {
      'playerName1': this.state.player1,
      'playerName2': this.state.player2
    }
    console.log(send);

    axios.post(BACKEND_URL+'/play', send)
      .then(response => {
          console.log(response.data);
          this.setState({
            result: response.data.result,
            gameMessage: response.data.message,
            gameLogs: response.data.logs
          })
          this.refreshUsers();

        })
      .catch(function(error) {
          console.log(error);
      })

  }

  showLogs = (event) => {
    this.setState({logsShown: 1})
  }

  hideLogs = (event) => {
    this.setState({logsShown: 0})
  }

  interpretResult(val) {
    if (val > 0){
      return "Player 1 won"
    } else if (val < 0){
      return "Player 2 won"
    } else {
      return "Draw"
    }
  }

  handleNewPlayerChange = (event) => {
    this.setState({newUser: event.target.value, newUserMessage:''});
    this.refreshUsers();
  }

  handleNewPlayerSubmit = (event) => {
    event.preventDefault();

    const send = {
      'name': this.state.newUser
    }
    console.log(send);

    axios.post(BACKEND_URL+'/register', send)
      .then(response => {
          console.log(response.data);
          this.setState({
            newUserMessage: response.data.message
          })
          this.refreshUsers();
        })
      .catch(function(error) {
          console.log(error);
      })

  }

  render() {
    return (
      
      <div className="App" class="main">

        <div class="container">
          <br></br>
          <h1 class="text-center">War: A card game</h1>
          <br></br>
        </div>

        <div class="container">
        <h2>Create New Player</h2>
          <form onSubmit={this.handleNewPlayerSubmit}>
            <label>
              Enter name of new player:
              <input type="text" value={this.state.value} onChange={this.handleNewPlayerChange} />
            </label>
            <input type="submit" value="Create New Player" />
          </form>
          <text class="container">{this.state.newUserMessage}</text>
        </div>
        <br></br>
        <br></br>


        <div class="container">
            <h2>Scoreboard:</h2>


        <div class="container">
          <text class="container">Select a player to display wins:  </text>
          <select class="custom-select btn-dark" value={this.state.selectedPlayer} onChange={this.getPlayerWins}>
            {this.state.players.map((player, id) => {
              return (
                <option value={player.name}>{player.name}</option>    
              )
            })}
          </select>
          {this.state.isPlayerSelected>0 && <text class="container">Wins: {this.state.selectedPlayerWins} </text>}
        </div>
        <br></br>

            <table class="table table-dark">
                <thead>
                    <tr>
                        <th>Player</th>
                        <th>Wins</th>
                    </tr>
                </thead>
                <tbody>
                { 
                    this.state.allPlayersWins.map((player, i) => {
                        return (
                            <tr>
                                <td>{player.name}</td>
                                <td>{player.wins}</td>
                            </tr>
                        )
                    })
                }
                </tbody>
            </table>
        </div>
        
        
        <br></br>
        <br></br>



        



        <div class="container">
          <h2>Simulate a round</h2>

          <text class="container"> Select Player 1: </text> 
          <select value={this.state.player1} onChange={this.setPlayer1}>
            {this.state.players.map((player, id) => {
              return (
                <option value={player.name}>{player.name}</option>    
              )
            })}
          </select>
          <br></br>
          <text class="container"> Select Player 2: </text> 
          <select value={this.state.player2} onChange={this.setPlayer2}>
            {this.state.players.map((player, id) => {
              return (
                <option value={player.name}>{player.name}</option>    
              )
            })}
          </select>
          <br></br>
          <br></br>

          <button class="btn btn-dark" onClick = {this.playGame}>Play Game</button>
          <br></br>
          <br></br>

          <text class="container">{this.state.gameMessage}</text>
          {this.state.result>=0 && this.state.logsShown===0 && <button class="btn btn-dark" onClick = {this.showLogs}>Show Game Summary</button>}
          {this.state.result>=0 && this.state.logsShown===1 && <button class="btn btn-dark" onClick = {this.hideLogs}>Hide Game Summary </button>}
          <br></br>
          <br></br>
          
          {this.state.logsShown==1 && 
            <div>
            <table class="table table-dark">
                <thead>
                    <tr>
                        <th>Round</th>
                        <th>Player 1 Card Count</th>
                        <th>Player 2 Card Count</th>
                        <th>Player 1 Played</th>
                        <th>Player 2 Played</th>
                        <th>Round Result</th>
                    </tr>
                </thead>
                <tbody>
                { 
                    this.state.gameLogs.map((player, i) => {
                        return (
                            <tr>
                                <td>{player.round}</td>
                                <td>{player.player1CardsCount}</td>
                                <td>{player.player2CardsCount}</td>
                                <td>{player.player1Card}</td>
                                <td>{player.player2Card}</td>
                                <td>{this.interpretResult(player.comparison)}</td>
                            </tr>
                        )
                    })
                }
                </tbody>
            </table>
        </div>
          }
        </div>
        <br></br>
        
      </div>
      
    )
  }
}