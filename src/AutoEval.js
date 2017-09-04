import React, {Component} from 'react';
import Button from 'muicss/lib/react/button';
import fetch from 'isomorphic-fetch';
import {server_url} from './config.js';
import {connect} from 'react-redux';

class AutoEval extends Component {
  constructor(props) {
    super(props);
    this.state = {
    }
    this.handleAutoEval = this.handleAutoEval.bind(this)
  }

  handleAutoEval(e) {
    let score = 1;
    if (e.target.value != 1) {
      score = e.target.value * this.props.difficulty;
    }
    fetch(server_url + 'api/score/update/' + this.props.user.id + '/' + this.props.objective.id + '/' + score,
    {method: "POST"})
    .then(response => response.json())
    .then((json) => {
      console.log(json.result);
    });
  }

  render() {
    return (
      <div id="autoeval">
        <h1>Auto-évaluation</h1>
        <h2>As-tu réussi cet exercice ? Sois honnête si tu veux progresser !</h2>
        <div className="buttons">
          <Button onClick={this.handleAutoEval} value='1' color="danger">Je n'avais pas réussi</Button>
          <Button onClick={this.handleAutoEval} value='3' color="primary">J'y étais presque..!</Button>
          <Button onClick={this.handleAutoEval} value='5' color="primary" style={{backgroundColor: "#4CAF50"}}>Oui, parfaitement</Button>
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
