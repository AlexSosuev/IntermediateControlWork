import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Toy[] toys = {
                new Toy(1, "конструктор", 5, 20),
                new Toy(2, "робот", 7, 30),
                new Toy(3, "кукла", 3, 50)
        };

        ToyLottery toyLottery = new ToyLottery();
        for (Toy toy : toys) {
            toyLottery.addPrizeToy(toy);
        }

        int numPrizes = 3; // Количество призовых игрушек для разыгрывания
        for (int i = 0; i < numPrizes; i++) {
            Toy drawnPrizeToy = toyLottery.drawPrizeToy();
            if (drawnPrizeToy != null) {
                try (FileWriter writer = new FileWriter("toy.txt", true)){
                    writer.write(String.format("Prize toys: %s (id: %d)%n", drawnPrizeToy.getName(), drawnPrizeToy.getId()));
                } catch (IOException e) {
                    e.printStackTrace();
                }

                drawnPrizeToy.decreaseQuantity();
            } else {
                System.out.println("No prize toys available");
                break;
            }
        }
    }
}