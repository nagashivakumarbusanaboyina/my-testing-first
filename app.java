class Employee {
    String name;
    int id;

    void display() {
        System.out.println("Employee Name: " + name);
        System.out.println("Employee ID: " + id);
    }
}

public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee();
        emp.name = "Naga";
        emp.id = 101;
        emp.display();
    }
}
