import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import ProfileScore from './ProfileScore.js'

class ProfileChapter extends Component {
  render() {
    let rows = [];
    // objectives = [{'objective': blabla, 'score': {objective, user, score}}, ...]
    this.props.objectives.forEach((obj) => {
      rows.push(
        <ProfileScore key={obj.objective.id} chapter={this.props.chapter} objective={obj.objective} score={obj.score.score}/>
      )
    });

    return (
      <div>
        <Link to={{pathname:'/exercices/chapitre/' + this.props.chapter.id, state:{chapter:this.props.chapter}}}>
          <div className="big-title" style={{color: this.props.chapter.color, display: "inline-flex"}}>Chapitre {this.props.chapter.nb}, {this.props.chapter.name}</div>
        </Link>
        <div className="scores-list" style={{display: "inline-flex"}}>
          <ul>
            {rows}
          </ul>
        </div>
      </div>
    )
  }
}

export default ProfileChapter
