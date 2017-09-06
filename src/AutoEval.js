import React, {Component} from 'react';
import Button from 'muicss/lib/react/button';
import fetch from 'isomorphic-fetch';
import {server_url} from './config.js';
import {connect} from 'react-redux';

class AutoEval extends Component {
  constructor(props) {
    super(props);
    this.handleAutoEval = this.handleAutoEval.bind(this)
    this.showText = this.props.handleShowTextAutoEval.bind(this);
  }

  handleAutoEval(e) {
    let score = 1;
    if (parseInt(e.target.value, 10) !== 1) {
      score = e.target.value * this.props.difficulty;
    }
    fetch(server_url + 'api/score/update/' + this.props.user.id + '/' + this.props.objective.id + '/' + score,
    {method: "POST"})
    .then(response => response.json())
    .then((json) => {});
    let text = "";
    if (parseInt(e.target.value, 10) === 1) {
      text = "Il n'y a que ceux qui n'essayent pas qui ne se trompent pas. Retente ta chance, ça va venir !";
    } else if (parseInt(e.target.value, 10) === 3) {
      text = "Tu es sur la voie, continue ! Tu gagnes " + score.toString() + " points dans cet objectif."
    } else {
      text = "Quel talent, bravo ! Tu gagnes " + score.toString() + " points dans cet objectif."
    }
    this.showText(true, text);
  }

  render() {
    return (
      <div id="autoeval" style={{display: this.props.user?"":"none"}}>
        <h1>Auto-évaluation</h1>
        <div style={{display: this.props.showText?"None":""}}>
          <h2>As-tu réussi cet exercice ? Sois honnête si tu veux progresser !</h2>
          <div className="buttons">
            <Button onClick={this.handleAutoEval} value='1' color="danger">Je n'avais pas réussi</Button>
            <Button onClick={this.handleAutoEval} value='3' color="primary">J'y étais presque..!</Button>
            <Button onClick={this.handleAutoEval} value='5' color="primary" style={{backgroundColor: "#4CAF50"}}>Oui, parfaitement</Button>
          </div>
        </div>
        <div style={{display: this.props.showText?"":"None", textAlign: "center"}}>
          {this.props.text}
        </div>
      </div>
    )
  }
}

function mapStateToProps(state) {
  return {
    user: state.user
  }
}

export default connect(mapStateToProps)(AutoEval);
