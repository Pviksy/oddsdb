import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;

import java.util.Observer;
import java.util.Observable;

public class DataVisualizationExample extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Create a data model
        DataModel dataModel = new DataModel();

        // Create a chart
        NumberAxis xAxis = new NumberAxis();
        NumberAxis yAxis = new NumberAxis();
        LineChart<Number, Number> chart = new LineChart<>(xAxis, yAxis);
        chart.setTitle("Data Visualization Example");

        // Create a series for the chart
        XYChart.Series<Number, Number> series = new XYChart.Series<>();
        series.setName("Data Series");

        // Add the series to the chart
        chart.getData().add(series);

        // Subscribe the chart to the data model
        dataModel.addObserver((observable, value) -> {
            Integer newValue = (Integer) value;
            series.getData().add(new XYChart.Data<>(dataModel.getCount(), newValue));
        });

        // Create a scene and add the chart to it
        Scene scene = new Scene(chart, 800, 600);
        scene.getStylesheets().add(getClass().getResource("style.css").toExternalForm());
        primaryStage.setScene(scene);
        primaryStage.show();

        // Start generating data
        dataModel.start();
    }

    private static class DataModel extends Observable {
        private int count = 0;
        private ObservableList<Integer> data = FXCollections.observableArrayList();

        public void start() {
            // Start generating data
            new Thread(() -> {
                while (true) {
                    try {
                        Thread.sleep(300);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    int value = (int) (Math.random() * 10);
                    data.add(value);
                    count++;

                    // Notify observers of the new data value
                    setChanged();
                    notifyObservers(value);
                }
            }).start();
        }

        public int getCount() {
            return count;
        }
    }
}
