import React, {Component} from 'react';
import Divider from 'muicss/lib/react/divider';
import ExerciceResume from './ExerciceResume.js';
import {server_url} from './config.js';
import {Link} from 'react-router-dom';

class ExercicesByObjective extends Component {
  constructor(props) {
    super(props);
    let chapter = {};
    let obj = {};
    if (props.location.state) {
      chapter = props.location.state.chapter;
      obj = props.location.state.obj;
    }
    this.state = {
      objective : obj,
      chapter: chapter,
      exercices: []
    };
  }

  componentDidMount() {
    let obj_id = this.props.match.params.objId.toString();
    fetch(server_url + 'api/objective/' + obj_id)
    .then(response => response.json())
    .then((json) => {
      this.setState({objective: json});
      fetch(server_url + 'api/chapter/' + json.chapter_id)
      .then(response => response.json())
      .then((chapterJson) => {this.setState({chapter: chapterJson})});
      fetch(server_url + 'api/objective/' + json.id + '/get_exercices')
      .then(response => response.json())
      .then((exoJson) => {this.setState({exercices: exoJson.result.sort((a,b) => a.difficulty - b.difficulty)})});
    });
  }

  render() {
    let rows = [];
    this.state.exercices.forEach((exercice) => {
      rows.push(
        <ExerciceResume exercice={exercice} chapter={this.state.chapter} obj={this.state.objective}></ExerciceResume>
      )
    });

    return (
      <div id="exercices-list">
        <Link to={{pathname:'/exercices/chapitre/' + this.state.chapter.id,state:{chapter:this.state.chapter}}}>
          <div className="big-title" style={{color: this.state.chapter.color}}>Chapitre {this.state.chapter.nb} : {this.state.chapter.name}</div>
        </Link>
        <Divider />
        <div className="big-title" style={{color: this.state.chapter.color}}>Objectif {this.state.objective.nb} : {this.state.objective.name}</div>
        <ul>
          {rows}
        </ul>
      </div>
    )
  }
}

export default ExercicesByObjective
