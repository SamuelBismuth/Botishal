package com.example.sam.botishal;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private EditText editText;
    private MessageAdapter messageAdapter;
    private ListView messagesView;
    private String botColor = getRandomColor();
    private String botName = "Botishal";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = (EditText) findViewById(R.id.editText);
        messageAdapter = new MessageAdapter(this);
        messagesView = (ListView) findViewById(R.id.messages_view);
        messagesView.setAdapter(messageAdapter);
    }

    public void sendMessage(View view) {
        String message = editText.getText().toString();
        if (message.length() > 0)
            editText.getText().clear();
        MemberData mebDat = new MemberData(getRandomName(), getRandomColor());
        Message message1 = new Message(message, mebDat, true);
        messageAdapter.add(message1);
        HTTPPost(message);
    }

    private String getRandomName() {
        String[] adjs = {"autumn", "hidden", "bitter", "misty", "silent", "empty", "dry", "dark", "summer", "icy", "delicate", "quiet", "white", "cool", "spring", "winter", "patient", "twilight", "dawn", "crimson", "wispy", "weathered", "blue", "billowing", "broken", "cold", "damp", "falling", "frosty", "green", "long", "late", "lingering", "bold", "little", "morning", "muddy", "old", "red", "rough", "still", "small", "sparkling", "throbbing", "shy", "wandering", "withered", "wild", "black", "young", "holy", "solitary", "fragrant", "aged", "snowy", "proud", "floral", "restless", "divine", "polished", "ancient", "purple", "lively", "nameless"};
        String[] nouns = {"waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning", "snow", "lake", "sunset", "pine", "shadow", "leaf", "dawn", "glitter", "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook", "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly", "feather", "grass", "haze", "mountain", "night", "pond", "darkness", "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder", "violet", "water", "wildflower", "wave", "water", "resonance", "sun", "wood", "dream", "cherry", "tree", "fog", "frost", "voice", "paper", "frog", "smoke", "star"};
        return (
                adjs[(int) Math.floor(Math.random() * adjs.length)] +
                        "_" +
                        nouns[(int) Math.floor(Math.random() * nouns.length)]
        );
    }

    private String getRandomColor() {
        Random r = new Random();
        StringBuffer sb = new StringBuffer("#");
        while (sb.length() < 7)
            sb.append(Integer.toHexString(r.nextInt()));
        return sb.toString().substring(0, 7);
    }

    private void HTTPPost(String question) {
        RequestQueue queue = Volley.newRequestQueue(this);
        String temp = fromQuestionToHTTPQuestion(question);
        String url = "http://172.20.10.5:8888/" + temp;
        StringRequest stringRequest = new StringRequest(
                Request.Method.POST,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        MemberData mebDat2 = new MemberData(botName, botColor);
                        Message message2 = new Message(fromHTTPAnswerToHebrew(response), mebDat2, false);
                        messageAdapter.add(message2);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e("That didn't work!", error.toString());
                    }
                });
        queue.add(stringRequest);
    }

    private String fromQuestionToHTTPQuestion(String question) {
        String answer = Integer.toString(question.charAt(0));
        for (int i = 1; i < question.length(); i++) {
            answer += "+" + Integer.toString(question.charAt(i));
        }
        return answer;
    }

    private String fromHTTPAnswerToHebrew(String answer) {
        String[] array = answer.split("\\+");
        String reformated = Character.toString((char) Integer.parseInt(array[0]));
        for (int i = 1; i < array.length; i++) {
            reformated += Character.toString((char) Integer.parseInt(array[i]));
        }
        return reformated;
    }

}

class MemberData {
    private String name;
    private String color;

    public MemberData(String name, String color) {
        this.name = name;
        this.color = color;
    }

    public MemberData() {
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return "MemberData{" +
                "name='" + name + '\'' +
                ", color='" + color + '\'' +
                '}';
    }
}