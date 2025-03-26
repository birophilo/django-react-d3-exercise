import React from "react";
import './OverallSentimentView.css'
import OverallSentimentChart from "../components/OverallSentimentChart";


const OverallSentimentView = (props) => {
  return (
    <div>
      <h3>Net sentiment chart - positive minus negative %</h3>
      <div className="subheading">(using D3)</div>
      <p className="button-container">
        <button onClick={() => props.handleSelectModel(null)}>All models</button>
        <button onClick={() => props.handleSelectModel('Model%203')}>Tesla Model 3</button>
        <button onClick={() => props.handleSelectModel('Model%20Y')}>Tesla Model Y</button>
        <button onClick={() => props.handleSelectModel('Enyaq')}>Skoda Enyaq</button>
      </p>
      <OverallSentimentChart data={props.dailyData} />
    </div>
  )
}

export default OverallSentimentView

