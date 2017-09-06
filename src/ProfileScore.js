import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './ProfileScore.css'
import MdCheck from 'react-icons/lib/md/check';

class ProfileScore extends Component {
  render() {
    var ProgressBar = require('react-progressbar.js')
    var Line = ProgressBar.Line;
    var containerStyle = {
      width: '20%',
      display: 'inline-flex',
      height: '10px',
      textAlign: "right",
      marginRight: "10px"
    };
    var options = {
      trailColor: 'white',
      color: '#E040FB',
      strokeWidth: 1,
      text: {
        style: {
          color: "white"
        }
      }
    }
    var progression = Math.min(this.props.score,100) / 100;
    var text = Math.min(this.props.score,100).toString() + "%";
    var link = '/exercices/objectif/' + this.props.objective.id.toString();
    let chapter = this.props.chapter;
    let obj = this.props.objective;
    let checked = this.props.score>=100;
    return (
      <Link to={{pathname:link, state:{chapter:chapter, obj:obj}}}>
        <li style={{backgroundColor: checked?"#4CAF50":this.props.chapter.color}}>
          <Line progress={progression} containerStyle={containerStyle} text={text} options={options} />
          {this.props.objective.name} <MdCheck style={{display: checked?"":"none", fontSize: "30px", marginLeft: "10px"}} />
        </li>
      </Link>
    )
  }
}

export default ProfileScore
