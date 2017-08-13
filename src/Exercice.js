import React, {Component} from 'react';
import Divider from 'muicss/lib/react/divider';
import './Exercice.css';
import Button from 'muicss/lib/react/button';
import {server_url} from './config.js';
import {Link} from 'react-router-dom';

class Exercice extends Component {
  constructor(props) {
    super(props);
    this.showSolution = this.showSolution.bind(this);
    let exercice = {};
    let obj = {};
    let chapter = {};
    if (props.location.state) {
      exercice = props.location.state.exercice;
      chapter = props.location.state.chapter;
      obj = props.location.state.obj;
    }

    this.state = {
      exercice: exercice,
      objective : obj,
      chapter: chapter,
      statement: "",
      solution: "",
      displaySol: false
    };
  }

  showSolution() {
    this.setState({displaySol: true});
  }

  componentDidMount() {
    fetch(server_url + 'api/exercice/' + this.props.match.params.exId)
    .then(response => response.json())
    .then((exercice) => {
      this.setState({exercice: exercice});
      //Get statement
      fetch(server_url + exercice.url)
      .then(response => response.json())
      .then((responseJson) => this.setState({statement: responseJson.statement, solution: responseJson.solution}));
      //Get current chapter
      fetch(server_url + 'api/chapter/' + exercice.chapter_id.toString())
      .then(response => response.json())
      .then(responseJson => this.setState({chapter: responseJson}));
      //Get objectives from server
      fetch(server_url + 'api/objective/' + exercice.obj_id.toString())
      .then(response => response.json())
      .then((responseJson) => this.setState({objective: responseJson}));
    });
  }

  render() {
    return (
      <div id="exercice">
        <Link to={{pathname:'/exercices/chapitre/' + this.state.chapter.id, state:{chapter:this.state.chapter}}}>
          <div className="big-title" style={{color: this.state.chapter.color}}>Chapitre {this.state.chapter.nb} : {this.state.chapter.name}</div>
        </Link>
        <Divider />
        <Link to={{pathname:'/exercices/objectif/' + this.state.objective.id, state:{chapter:this.state.chapter, obj:this.state.objective}}}>
          <div className="big-title" style={{color: this.state.chapter.color}}>Objectif {this.state.objective.nb} : {this.state.objective.name}</div>
        </Link>
        <Divider />
        <div className="big-title" style={{color: this.state.chapter.color}}>{this.state.exercice.name}</div>
        <h1>Difficulté : {this.state.exercice.difficulty}</h1>
        <div id="statement" style={{borderColor: this.state.chapter.color}}>
          <h1>Énoncé :</h1>
          <div dangerouslySetInnerHTML={{__html: this.state.statement}}></div>
          <br/>
          <Button color="primary" onClick={this.showSolution} style={{display: this.state.displaySol ? 'none' : ''}}>J'ai fini et je veux voir la solution</Button>
        </div>
        <div id="solution" style={{borderColor: this.state.chapter.color, display: this.state.displaySol ? '' : 'none'}} >
          <h1>Solution</h1>
          <div dangerouslySetInnerHTML={{__html: this.state.solution}}></div>
          <div style={{display: "None"}} id="autoeval">
            <h1>Auto-évaluation</h1>
            <h2>As-tu réussi cet exercice ? Sois honnête si tu veux progresser !</h2>
            <div className="buttons">
              <Button color="danger">Je n'avais pas réussi</Button>
              <Button color="primary">J'y étais presque..!</Button>
              <Button color="primary" style={{backgroundColor: "#4CAF50"}}>Oui, parfaitement</Button>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Exercice
