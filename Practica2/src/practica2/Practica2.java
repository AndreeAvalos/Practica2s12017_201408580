/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2;

import Interfaz.Menu;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author Andree
 */
public class Practica2 {

    /**
     * @param args the command line arguments
     */
    public static OkHttpClient webClient = new OkHttpClient();

    public static void main(String[] args) {
        // TODO code application logic here
        Menu menu = new Menu();
        menu.show();

    }

    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.1.1.2:8080/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
        } catch (Exception ex) {
        }
        return null;
    }

}
