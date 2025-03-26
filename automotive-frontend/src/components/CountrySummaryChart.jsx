import React from 'react'
import './CountrySummaryChart.css'
import '/node_modules/flag-icons/css/flag-icons.min.css'

const CountrySummaryChart = (props) => {

  const dataCurrentYear = props.chartData.data[props.chartData.data.length - 1]

  const positive = dataCurrentYear.positive
  const neutral = dataCurrentYear.neutral
  const negative = dataCurrentYear.negative

  const total = positive + neutral + negative

  const positiveDec = positive / total
  const neutralDec = neutral / total
  const negativeDec = negative / total

  const positivePc = Math.round(positiveDec * 100)
  const neutralPc = Math.round(neutralDec * 100)
  const negativePc = Math.round(negativeDec * 100)

  const maxWidth = 200

  return (
    <div className="country-summary-chart-container">
      <div className="country-summary-image-container">
        <img className="country-image" src={`../flags/${props.chartData.countryCode}.svg`} />
      </div>
      <div className="country-summary-bars-container">
        <div className="bar-wrapper">
          <div className="bar-label">{positivePc}</div>
          <div
            className="positive-bar country-summary-bar"
            style={{width: `${positiveDec * maxWidth}px`}}
            title={`${positivePc}% positive`}
          ></div>
        </div>
        <div className="bar-wrapper">
          <div className="bar-label">{neutralPc}</div>
          <div
            className="neutral-bar country-summary-bar"
            style={{width: `${neutralDec * maxWidth}px`}}
            title={`${neutralPc}% neutral`}
          ></div>
        </div>
        <div className="bar-wrapper">
          <div className="bar-label">{negativePc}</div>
          <div
            className="negative-bar country-summary-bar"
            style={{width: `${negativeDec * maxWidth}px`}}
            title={`${negativePc}% negative`}
          ></div>
        </div>
      </div>
    </div>
  )
}

export default CountrySummaryChart