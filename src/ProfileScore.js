import React, {Component} from 'react';
import './ProfileScore.css'

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
    return (
      <div>
        <li style={{backgroundColor: this.props.color}}>
          <Line progress={progression} containerStyle={containerStyle} text={text} options={options} />
          {this.props.objective.name}
        </li>
      </div>
    )
  }
}

export default ProfileScore
