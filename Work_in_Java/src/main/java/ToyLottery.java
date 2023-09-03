import java.util.ArrayList;
import java.util.List;

class ToyLottery {
    private final List<Toy> prizeToys;

    public ToyLottery() {
        prizeToys = new ArrayList<>();
    }

    public void addPrizeToy(Toy toy) {
        prizeToys.add(toy);
    }

    public Toy drawPrizeToy() {
        int totalWeight = prizeToys.stream().mapToInt(Toy::getWeight).sum();
        int random = (int) (Math.random() * totalWeight) + 1;

        for (Toy toy : prizeToys) {
            random -= toy.getWeight();
            if (random <= 0) {
                prizeToys.remove(toy);
                return toy;
            }
        }
        return null;
    }
}