import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {

    public static void main(String[] args) throws IOException, InterruptedException {

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://eu-offering-api.kambicdn.com/offering/v2018/ubdk/listView/cycling/all/all/all/competitions.json?lang=da_DK&market=DK&client_id=2&channel_id=1&ncid=1675880965142&useCombined=true"))
                .header("authority", "eu-offering-api.kambicdn.com")
                .header("accept", "application/json, text/javascript, */*; q=0.01")
                .header("accept-language", "da-DK,da;q=0.9")
                .header("origin", "https://www.unibet.dk")
                .header("referer", "https://www.unibet.dk/")
                .header("sec-ch-ua", "^\\^Not_A")
                .header("sec-ch-ua-mobile", "?0")
                .header("sec-ch-ua-platform", "^\\^Windows^^")
                .header("sec-fetch-dest", "empty")
                .header("sec-fetch-mode", "cors")
                .header("sec-fetch-site", "cross-site")
                .header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
                .method("GET", HttpRequest.BodyPublishers.noBody())
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
