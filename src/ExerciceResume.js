import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './ExerciceResume.css';

class ExerciceResume extends Component {
  render() {
    let exercice = this.props.exercice;
    let chapter = this.props.chapter;
    let obj = this.props.obj;
    let link = '/exercices/' + exercice.id;
    return (
      <Link to={{pathname:link,state:{chapter:chapter, obj:obj, exercice:exercice}}}>
        <li style={{backgroundColor: chapter.color}}>
          <span>Difficulté : {exercice.difficulty} &nbsp;</span>
          <span className="exercice-name">&nbsp; {exercice.name}</span>
        </li>
      </Link>
    )
  }
}

export default ExerciceResume
