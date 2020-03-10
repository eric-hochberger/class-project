# PredicT Project for Northwestern Statistics 359: Topics in Statistics

## Final Report

### Summary
I worked on training models and developing a front-end dashboard for PredicT throughout the quarter. These fit into the cloud-based infrastructure framework that is proposed in the "Model Training/Deployment" and "Downstream Tasks" sections. Through this project I gained experience in using sci-kit learn with time series data, and strongly developed my knowledge of Amazon Web Services and its integration with Tableau. 

Over the course of the quarter, I did extensive research in order to identify what the best dashboard option would be for PredicT, a time-series data prediction product, which is being developed according to a proposed cloud-based data science infrastructure. I isolated Tableau as the best option due to its interactive nature, clear and simple design and capability in connecting with AWS data sources, which are central to PredicT's functionality. I deployed a Tableau dashboard on the AWS cloud via Tableau Server and developed a local template dashboard to be used once PredicT's data lake is functional. 

The infrastructure of PredicT is intended to be such that each module can be containerized and deployed to the cloud. It was thus important that each individual module be able to be deployed and connected via a singular cloud provider hence the emphasis on Amazon Web Services. Examples include deploying and training models on Amazon's SageMaker or utilizing an AWS Data Lake in addition to the previously cited example of Tableau. 

The next steps in order to improve upon the Data Visualization module include connecting directly to Amazon SageMaker once Tableau releases the [forthcoming SageMaker native data connector](https://www.tableau.com/about/blog/2018/10/our-ongoing-work-aws-support-your-cloud-analytics-journey-95959). An additional improvement would be to automatically detect how granular the submitted time-series data is and automatically adjust the "Date Granularity" field introduced below accordingly.   

### Reproducibility
1. Obtain a Tableau Server [license key](https://buy.tableau.com/#server)

2. Download the Amazon Athena driver according to your JDK specifications [here](https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html)

3. Follow [this tutorial](https://aws-quickstart.s3.amazonaws.com/quickstart-tableau-server/doc/tableau-server-on-the-aws-cloud.pdf) in order to deploy the Tableau Server on the AWS cloud using Option 2 and using "0.0.0.0/0" as the "Source CIDR for Access" and your Tableau key from above. (Note: there may be some additional steps in order to make sure an EC2 instance can be launched, but the stack deployment will prompt these)

4. Connect via [Amazon Athena](https://www.tableau.com/about/blog/2017/5/connect-your-s3-data-amazon-athena-connector-tableau-103-71105) to S3 bucket containing time series data and predictions

5. Create a new sheet in Tableau

6. Create a "[Date Granularity](https://evolytics.com/blog/tableau-201-change-date-aggregation-using-parameters/)" field according to steps 1 and 2

7. Ensure "Date Granularity" is continuous, drag to Columns and change the date option to "Exact Date"
![Screen Shot 2020-03-09 at 2 27 47 PM](https://user-images.githubusercontent.com/55408707/76249889-37018000-6212-11ea-971b-b9299093144e.png)


8. Drag time-series data (ex: "Actual", "Prediction") to Rows, and change the aggregate measure to "Average"

![Screen Shot 2020-03-09 at 2 30 28 PM](https://user-images.githubusercontent.com/55408707/76250061-8ba4fb00-6212-11ea-854c-c31daa76f5e8.png)

9. Select "Show Parameter Control" for the "Date Granularity" parameter which will enable a drop-down menu for "Date Granularity"
![Screen Shot 2020-03-09 at 2 33 00 PM](https://user-images.githubusercontent.com/55408707/76250314-1ab21300-6213-11ea-8207-ab7f44808b0f.png)
![Screen Shot 2020-03-09 at 2 36 24 PM](https://user-images.githubusercontent.com/55408707/76250976-41247e00-6214-11ea-91b2-536e3e42d58a.png)

10. Create new dashboard and drag and drop previously-created sheet

TableauExample.twbx serves as a local template, using [this data](https://github.com/eric-hochberger/class-project/blob/master/hourly-energy-consumption/AEP_hourly.csv). 

For the model training, RandomForest.py contains the code I used to train a random forest regression model on monthly energy consumption data accessed here: https://www.kaggle.com/robikscube/hourly-energy-consumption/version/3. The code is runnable as long as the hourly-energy-consumption folder is in the working directory. Note that the output is a trained model file which takes up 4 GB. 

Link to saved model: https://drive.google.com/file/d/1zohR0Q08IoI4Bi1KdVo_QiTVecHE2W-E/view?usp=sharing


