# Stock Ticker API usage and testing

Uses [Free Stock Market API and Financial Statements](https://site.financialmodelingprep.com/developer/docs) to gather data and evaluate worthwhile entry and exit points. 

# Setup and Dependencies

```
pip install pytest
```

To run these tests you will need a (Free) API Key. To create that key:
- Visit: [Free Stock Market API and Financial Statements](https://site.financialmodelingprep.com/developer/docs) and sign up for an account
- Go to "Dashboard" and your API key will be present at the top.
- Copy your API key and store it with your environment variables as "API_KEY"
- I use PyCharm for my IDE, to set environment variables:
  - Select the dropdown next to the run and debug buttons that says either "Current File" or shows your last run test
  - Select "Edit Configurations"
  - Select "Edit Configuration Templates"
  - Select "Pytest"
  - Add "API_KEY" env variable with the value of the key you created.
  - Save your template and clear out any old runs that may be leveraging old configs.
  - Execute your tests.
