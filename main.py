from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import shutil
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd
import time
import os
import logging
####

#####



# Setup logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress warnings from pandas
pd.options.mode.chained_assignment = None

# Initialize web driver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

def table_to_csv(page, classi, ticker, csv_name, obj_num=0, ticker_name=None):
    try:
        df = pd.read_html(page, attrs={"class": classi})[obj_num]
        df['Ticker'] = ticker
        df['Ticker_Name'] = ticker_name
        file_path = f"{csv_name}.csv"
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', index=False, header=False)
        else:
            df.to_csv(file_path, mode='w', index=False)
    except Exception as e:
        logging.error(f"Error processing {ticker}: {str(e)}")
        return False
    return True


def process_tickers():
    start_time = time.time()
    with open('tickers.csv', 'r') as f:
        tickers = f.read().split(',')

    for num, ticker in enumerate(tickers):
        try:
            driver.get(f"{ticker}")
            #revenue
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='revenue', obj_num=1)
            #cost-goods-sold
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='cost-goods-sold', obj_num=1)
            #gross-profit
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='gross-profit', obj_num=1)
            #research-development-expenses
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='research-development-expenses', obj_num=1)
            #selling-general-administrative-expenses
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker, csv_name='selling-general-administrative-expenses', obj_num=1)
            #operating-expenses
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='operating-expenses', obj_num=1)
            #operating-income
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='operating-income', obj_num=1)
            #total-non-operating-income-expense
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-non-operating-income-expense', obj_num=1)
            #pre-tax-income
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='pre-tax-income', obj_num=1)
            #total-provision-income-taxes
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-provision-income-taxes', obj_num=1)
            #income-after-taxes
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='income-after-taxes', obj_num=1)
            #income-from-continuous-operations
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='income-from-continuous-operations', obj_num=1)
            #net-income
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='net-income', obj_num=1)
            #ebitda
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='ebitda', obj_num=1)
            #ebit
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker, csv_name='ebit',obj_num=1)
            #basic-shares-outstanding
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='basic-shares-outstanding', obj_num=1)
            #shares-outstanding
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='shares-outstanding', obj_num=1)
            #eps-basic-net-earnings-per-share
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='eps-basic-net-earnings-per-share', obj_num=1)
            #eps-earnings-per-share-diluted
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='eps-earnings-per-share-diluted', obj_num=1)
            #cash-on-hand
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='cash-on-hand', obj_num=1)
            #receivables-total
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='receivables-total', obj_num=1)
            #inventory
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='inventory', obj_num=1)
            ##total-current-asset
            ##table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-current-asset', obj_num=1)
            #net-property-plant-equipment
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker, csv_name='net-property-plant-equipment', obj_num=1)
            #long-term-investments
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='long-term-investments', obj_num=1)
            #other-long-term-assets
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='other-long-term-assets', obj_num=1)
            #total-long-term-assets
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-long-term-assets', obj_num=1)
            #total-assets
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-assets', obj_num=1)
            #total-current-liabilities
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-current-liabilities', obj_num=1)
            #long-term-debt
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='long-term-debt', obj_num=1)
            #other-non-current-liabilities
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='other-non-current-liabilities', obj_num=1)
            #total-long-term-liabilities
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-long-term-liabilities', obj_num=1)
            #total-liabilities
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker, csv_name='total-liabilities', obj_num=1)
            #common-stock-net
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='common-stock-net', obj_num=1)
            #retained-earnings-accumulated-deficit
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker, csv_name='retained-earnings-accumulated-deficit', obj_num=1)
            #comprehensive-income
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='comprehensive-income', obj_num=1)
            #total-share-holder-equity
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-share-holder-equity', obj_num=1)
            #total-liabilities-share-holders-equity
            #table_to_csv(page=driver.page_source, classi='historical_data_table table', ticker=ticker,csv_name='total-liabilities-share-holders-equity', obj_num=1)
            #current-ratio
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='current-ratio')
            #debt-equity-ratio
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='debt-equity-ratio')
            #gross-margin
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='gross-margin')
            #operating-margin
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='operating-margin')
            #ebit-margin
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='ebit-margin')
            #pre-tax-profit-margin
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='pre-tax-profit-margin')
            #net-profit-margin
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker,csv_name='net-profit-margin')
            #roe
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker, csv_name='roe')
            #return-on-tangible-equity
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker, csv_name='return-on-tangible-equity')
            #roa
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker, csv_name='roa')
            #roi
            #table_to_csv(page=driver.page_source, classi='table', ticker=ticker, csv_name='roi')

            print(num,f'Stuck in ticker: {ticker}')
            logging.info(f"Processed {ticker}")
            time.sleep(20)  # Adjust as needed
        except Exception as e:
            logging.error(f"Stuck in ticker {ticker}: {str(e)}")
        finally:
            logging.info(f"Completed processing {num + 1} tickers")

    driver.close()
    logging.info(f"Execution time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    process_tickers()