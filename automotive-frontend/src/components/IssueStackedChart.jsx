import React from "react"
import './IssueStackedChart.css'
import {
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from "recharts"
 
const IssueStackedChart = (props) => {

  // select only the past 6 months for display purposes as recent dataset is larger
  const data = props.chartData.data.slice(
    props.chartData.data.length - 6,
    props.chartData.data.length
  )

  const rechartData = data.map(item => {
    const total = item.positive + item.neutral + item.negative
    const positivePc = Math.floor((item.positive / total) * 100)
    const neutralPc = Math.floor((item.neutral / total) * 100)
    const negativePc = Math.floor((item.negative / total) * 100)

    return {
      name: item.month,
      positive: positivePc,
      neutral: neutralPc,
      negative: negativePc
    }

  })
 
    return (
      <div className="issue-stacked-chart-container">
        <h4 className="stacked-chart-heading">{props.chartData.feedbackSubcategory}</h4>
        <AreaChart width={300} height={160} data={rechartData}>
          <CartesianGrid />
          <XAxis dataKey="name" />
          <YAxis label={{ fontSize: '0.3rem' }} />
          <Tooltip />
          <Area
            dataKey="negative"
            stackId="1"
            stroke="red"
            fill="red"
          />
          <Area
            dataKey="neutral"
            stackId="1"
            stroke="#e8cf3f"
            fill="#e8cf3f"
          />
          <Area
            dataKey="positive"
            stackId="1"
            stroke="#0f8c0f"
            fill="#0f8c0f"
          />
        </AreaChart>
      </div>
    )
}
 
export default IssueStackedChart