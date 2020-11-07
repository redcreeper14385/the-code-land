package fundamentals;

public class Strings {

	public static void main(String[] args) {
		
//--- String Syntax -----//
String myString = "My String";
//String Concatenation
String str1 = "Hack";
String str2 = "toberfest";
//Method 1 : Using concat
String str3 = str1.concat(str2);
System.out.println(str3);
//Method 2 : Using "+" operator
String str4 = str1 + str2;
System.out.println(str4);

 //Length of a String
String myString = "CODE_LAND"
System.out.println("Length of String: " + myString.length());


//Index of a given character
System.out.println("Index of character 'S': " + myString.indexOf('S'));


//Compare to a String
System.out.println("Compare To 'CODELAND': " + myString.compareTo("CODELAND"));
//Compare to - Ignore case
System.out.println("Compare To 'codeland' - Case Ignored: " + myString.compareToIgnoreCase("codeland"));



//Check if String contains a sequence
String string = "CodeLand";
System.out.println("Contains sequence 'Land': " + string.contains("Land"));



//Check if ends with a particular sequence
String string = "CodeLand";
System.out.println("EndsWith character 'd': " + string.endsWith("d"));



//Replace Rock with the word Duke
String myString = "CodeLand";
System.out.println("Replace 'CodeLand' with 'Hacktoberfest': " + myString.replace("CodeLand", "Hacktoberfest"));


//Convert to LowerCase
String myString = "CodeLand";
System.out.println("Convert to LowerCase: " + myString.toLowerCase());
//Convert to UpperCase
System.out.println("Convert to UpperCase: " + myString.toUpperCase());

		
}

}
