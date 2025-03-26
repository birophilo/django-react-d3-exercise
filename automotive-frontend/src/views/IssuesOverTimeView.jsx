import React from 'react'
import './IssuesOverTimeView.css'
import IssueStackedChart from '../components/IssueStackedChart'


const IssuesOverTimeView = (props) => {

  return (
    <div>
      <h3>Feedback by Category, last 6 months</h3>
      <div className="subheading">(using Recharts library)</div>
      <div className="issue-chart-view-container">
        {props.subcategoryData.map(subcategory => 
          <div >
            <IssueStackedChart chartData={subcategory} key={subcategory.feedbackSubcategory} />
          </div>
        )}
      </div>
    </div>
  )
}

export default IssuesOverTimeView