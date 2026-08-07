package Java;
class MergeStrings {

    // Outputs a String that takes in String word1 and String word2.
    public String mergeAlternately(String word1, String word2) {
        System.out.println("word1: " + word1);
        System.out.println("word2: " + word2);
        return "";
    }

    public static void main(String[] args) {
        MergeStrings mergeStrings = new MergeStrings();
        String result = mergeStrings.mergeAlternately("abc", "pqr");
        System.out.println("Merged string: " + result);
    }
}