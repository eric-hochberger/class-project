# PredicT Project for Northwestern Statistics 359: Topics in Statistics

## Final Report

### Summary
I worked on training models and developing a front-end dashboard for PredicT throughout the quarter. These fit into the cloud-based infrastructure framework that is proposed in the "Model Training/Deployment" and "Downstream Tasks" sections. Through this project I gained experience in using sci-kit learn with time series data, and strongly developed my knowledge of Amazon Web Services and its integration with Tableau. 

Over the course of the quarter, I did extensive research in order to identify what the best dashboard option would be for PredicT, a time-series data prediction product, which is being developed according to a proposed cloud-based data science infrastructure. I isolated Tableau as the best option due to its interactive nature, clear and simple design and capability in connecting with AWS data sources, which are central to PredicT's functionality. I deployed a Tableau dashboard on the AWS cloud via Tableau Server and developed a local template dashboard to be used once PredicT's data lake is functional. 






RandomForest.py contains the code I used to train a random forest regression model on monthly energy consumption data accessed here: https://www.kaggle.com/robikscube/hourly-energy-consumption/version/3

Link to saved model: https://drive.google.com/file/d/1zohR0Q08IoI4Bi1KdVo_QiTVecHE2W-E/view?usp=sharing

### Reproducibility
1. Obtain a Tableau Server [license key](https://buy.tableau.com/#server)

2. Download the Amazon Athena driver according to your JDK specifications [here](https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html)

3. Follow [this tutorial](https://aws-quickstart.s3.amazonaws.com/quickstart-tableau-server/doc/tableau-server-on-the-aws-cloud.pdf) in order to deploy the Tableau Server on the AWS cloud using Option 2 and using "0.0.0.0/0" as the "Source CIDR for Access" and your Tableau key from above. (Note: there may be some additional steps in order to make sure an EC2 instance can be launched, but the stack deployment will prompt these)

4. Create a new Tableau dashboard

5. 
