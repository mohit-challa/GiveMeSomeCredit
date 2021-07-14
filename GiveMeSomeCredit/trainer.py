
    def retrieve_data(self)
        # get data
        df = get_data_using_pandas()
        # holdout
        self.X_train, self.X_test, self.y_train, self.y_test = holdout(df)

    def evaluate_pipeline(self):
        # make prediction for metrics
        y_pred = self.pipeline.predict(self.X_test)
        # evaluate metrics
        self.rmse = compute_rmse(y_pred, self.y_test)
        print(f"rmse: {self.rmse}")

    def train(self):
        # step 1 : get data
        self.retrieve_data()
        # step 2 : create pipeline
        #model = get_model()
        self.pipeline = get_pipeline()
        # step 3 : train
        self.pipeline.fit(self.X_train, self.y_train)
        # step 4 : evaluate perf
        self.evaluate_pipeline()
        # step 5 : save the trained model
        #joblib.dump(self.pipeline, "model.joblib")

        # step 6 : upload model to gcp
        #save_model_to_gcp()

        # return the pipeline to identify the hyperparams
        return self.pipeline

