import React from 'react'
import './CountrySummaryView.css'
import CountrySummaryChart from '../components/CountrySummaryChart'


const CountrySummaryView = (props) => {

  return (
    <>
      <h3>Country Sentiment Summary (%), 2025 to date</h3>
      <div className="subheading">(using React components)</div>
      <div className="country-summary-view-container">
        {props.countryData.map(country => 
          <CountrySummaryChart chartData={country} key={country.countryCode} />
        )}
      </div>
    </>
  )
}

export default CountrySummaryView