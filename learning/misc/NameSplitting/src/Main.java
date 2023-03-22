public class Main {

    public static void main(String[] args) {

        String riderName = "JOHANNESSEN Tobias Halland";
        String riderName2 = "VAN AERT Wout";

        correctNameOrder(riderName);
        correctNameOrder(riderName2);

    }

    static void correctNameOrder(String riderName) {
        String[] name = riderName.split(" ");
        String firstname;
        String lastname;
        if (name.length == 2) {
            firstname = name[1];
            lastname = name[0];
        } else if (name.length == 3) {
            firstname = name[name.length-1];
            lastname = name[0] + " " + name[1];
        } else {
            firstname = name[name.length-1];
            lastname = name[0] + " " + name[1] + " " + name[2];
        }

        System.out.println(firstname + " " + lastname);
    }
}
