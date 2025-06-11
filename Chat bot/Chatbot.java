import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Chatbot {
    private Map<String, String> responses;

    public Chatbot() {
        responses = new HashMap<>();
        initializeResponses();
    }

    private void initializeResponses() {
        responses.put("hi|hello|hey", "Hello! How can I assist you today?");
        responses.put("how are you", "I'm doing great, thanks for asking! How about you?");
        responses.put("what is your name", "I'm Grok, your friendly chatbot!");
        responses.put("bye|goodbye", "Goodbye! Have a great day!");
        responses.put(".*", "Sorry, I didn't understand that. Can you rephrase?");
    }

    public String getResponse(String input) {
        String cleanedInput = input.toLowerCase().trim();
        
        for (Map.Entry<String, String> entry : responses.entrySet()) {
            Pattern pattern = Pattern.compile(entry.getKey(), Pattern.CASE_INSENSITIVE);
            Matcher matcher = pattern.matcher(cleanedInput);
            if (matcher.matches()) {
                return entry.getValue();
            }
        }
        return responses.get(".*");
    }

    public void start() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Chatbot started. Type 'exit' to quit.");

        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("exit")) {
                System.out.println("Chatbot: Goodbye!");
                break;
            }

            String response = getResponse(userInput);
            System.out.println("Chatbot: " + response);
        }
        
        scanner.close();
    }

    public static void main(String[] args) {
        Chatbot chatbot = new Chatbot();
        chatbot.start();
    }
}