import React, { useState, useEffect } from 'react';
import * as d3 from 'd3'


const OverallSentimentChart = (props) => {

  const rawDataReal = [...props.data].slice(20, props.data.length)

  const rawData = rawDataReal.map(item => {
    const total = item.positive + item.neutral + item.negative
    const net = item.positive - item.negative
    const sentiment = Math.round((net / total) * 100)
    return {date: item.post_date, value: sentiment}
  })

  const formattedData = rawData.map(d => {
    return {date: d3.timeParse("%Y-%m-%d")(d.date), value: d.value}
  })

  const data = formattedData

  useEffect(() => {

    // delete SVG before repainting
    d3.select("#overall-sentiment-chart").selectAll("*").remove()

    const baseWidth = 760
    const baseHeight = 400

    // set the dimensions and margins of the graph
    const margin = {top: 10, right: 30, bottom: 30, left: 60},
        width = baseWidth - margin.left - margin.right,
        height = baseHeight - margin.top - margin.bottom;

    // append the svg object to the body of the page
    const svg = d3.select("#overall-sentiment-chart")
      .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // Add X axis (date format)
    const x = d3.scaleTime()
      .domain(d3.extent(data, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x));

    const positiveY = d3.max(data, function(d) { return +d.value; })
    const negativeY = d3.min(data, function(d) { return +d.value; })

    const useY = Math.abs(positiveY) > Math.abs(negativeY) ? positiveY : negativeY

    // Add Y axis
    const y = d3.scaleLinear()
      .domain([useY, -useY])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // zero line
    svg.append("line")
      .attr("x1", 1)
      .attr("y1", height / 2)
      .attr("x2", width)
      .attr("y2", height / 2)
      .style("stroke", "#ededed")
      .style("stroke-width", 2)

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "seagreen")
      .attr("stroke-width", 2.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.value) })
        )

  }, [props.data])

  return <div id="overall-sentiment-chart"></div>

}

export default OverallSentimentChart

