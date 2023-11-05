package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private int insertedQuarters = 0;
    private Map<String, Drink> drinks = new HashMap<>();

    @Override
    public void insertQuarter() {
        insertedQuarters++;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (!drinks.containsKey(name)) {
            throw new UnknownDrinkException();
        }

        Drink drink = drinks.get(name);

        if (insertedQuarters < 3) {
            throw new NotEnoughMoneyException();
        }

        // Deduct the cost of the drink
        insertedQuarters -= 3;

        return drink;
    }

    public void addDrink(String name, Drink drink) {
        drinks.put(name, drink);
    }

    public static VendingMachine getInstance() {
        VendingMachineImpl vm = new VendingMachineImpl();

        // Define the available drinks
        Drink scottCola = new ScottCola();
        Drink karenTea = new KarenTea();

        vm.addDrink("ScottCola", scottCola);
        vm.addDrink("KarenTea", karenTea);

        return vm;
    }
}
