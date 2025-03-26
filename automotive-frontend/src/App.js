import axios from 'axios'
import { useEffect, useState } from 'react'
import OverallSentimentView from './views/OverallSentimentView'
import CountrySummaryView from './views/CountrySummaryView'
import IssuesOverTimeView from './views/IssuesOverTimeView';


const countryCodes = ['UK', 'DE', 'DK', 'IT', 'FR', 'ES', 'US', 'NL', 'NO', 'BE']

const feedbackSubcategories = [
  'Quality',
  'Product Concern/Query',
  'Price',
  'Battery',
  'Test Drive',
  'Charging Experience'
]


const App = () => {

  const [dailyData, setDailyData] = useState(null)
  const [countrySummaryData, setCountrySummaryData] = useState([])
  const [subcategoryData, setSubcategoryData] = useState([])

  const [model, setModel] = useState(null)

  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const handleSelectModel = (model) => {
    setModel(model)
  }

  useEffect(() => {
    const fetchDailyData = async () => {
      const params = model ? `?groupBy=day&model=${model}` : '?groupBy=day'
      try {
        const response = await axios.get(
          `http://localhost:8000/feedbacks${params}`
        );
        setDailyData(response.data)
      } catch (error) {
        setError(error.message)
      } finally {
        setLoading(false)
      }
    };

    fetchDailyData();

  }, [model])

  useEffect(() => {
    const fetchCountryCodeData = async () => {
      try {
        const responses = await Promise.all(
          countryCodes.map(countryCode => axios.get(
            'http://localhost:8000/feedbacks',
            { params: { groupBy: 'year', countryCode: countryCode } }
          ))
        );

        const mappedData = responses.map((response, index) => ({
          countryCode: countryCodes[index],
          data: response.data,
        }));

        setCountrySummaryData(mappedData);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCountryCodeData();
  }, [])

  useEffect(() => {
    const fetchSubcategoryData = async () => {
      try {

        const responses = await Promise.all(
          feedbackSubcategories.map(subcategory => axios.get(
            'http://localhost:8000/feedbacks',
            { params: { groupBy: 'month', feedbackSubcategory: subcategory } }
          ))
        );

        const mappedData = responses.map((response, index) => ({
          feedbackSubcategory: feedbackSubcategories[index],
          data: response.data,
        }));

        setSubcategoryData(mappedData);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSubcategoryData();
  }, [])

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error}</p>

  return (
    <div>
      <OverallSentimentView handleSelectModel={handleSelectModel} dailyData={dailyData} />
      <IssuesOverTimeView subcategoryData={subcategoryData} />
      <CountrySummaryView countryData={countrySummaryData} />
    </div>
  )
}

export default App;
