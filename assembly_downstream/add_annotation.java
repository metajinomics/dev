//this code add annotation (organism and function) at the end of the count table
//javac add_annotation.java
// usage: java add_annotation.java normal_counts.txt mgm4675652.3_organism_KEGG.tab mgm4675652.3_function_KEGG.tab
//java add_annotation normal_counts.txt mgm4675652.3_organism_KEGG_nopipe.tab mgm4675652.3_function_KEGG_nopipe.tab big_table.txt

import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.lang.Object;
class add_annotation {
    public static void main(String[] args){
	//read organism then put in map
	HashMap <String,String> org = new HashMap<String,String>();
	File orFile = new File(args[1]);
	try{
	    Scanner orFile_scan = new Scanner(orFile);
	    while(orFile_scan.hasNextLine()){
		String line = orFile_scan.nextLine();
		String[] parts = line.split("\t");
		if (parts.length > 11){
		    org.put(parts[0],parts[12]);
		    //System.out.println(parts[12]);
		}
	    }
	}catch (FileNotFoundException e){
	    e.printStackTrace();
	}

	//read function then put in map
	HashMap <String,ArrayList<String>> fun = new HashMap<String,ArrayList<String>>();
        File funFile = new File(args[2]);
        try{
            Scanner funFile_scan = new Scanner(funFile);
            funFile_scan.nextLine();
            while(funFile_scan.hasNextLine()){
                String line = funFile_scan.nextLine();
                String[] parts = line.split("\t");
                if (parts.length > 11){
                	double tempcomp = Double.parseDouble(parts[11]);
                	if(fun.containsKey(parts[0])){
                		double comp = Double.parseDouble(fun.get(parts[0]).get(1));
                		if(comp < tempcomp){
                			ArrayList<String> temp = new ArrayList<String>();
                			temp.add(parts[12]);
                			temp.add(parts[11]);
                			fun.put(parts[0],temp);
                		}
                	}else{
                		ArrayList<String> temp = new ArrayList<String>();
                		temp.add(parts[12]);
                		temp.add(parts[11]);
                		//System.out.println(parts[11]);
                    	fun.put(parts[0],temp);
                    }
                }
            }
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }
	//read counts to process merge
	File countFile = new File(args[0]);
	try{
            Scanner coFile_scan = new Scanner(countFile);
	    PrintStream Result = new PrintStream(args[3]);
	    Result.println(coFile_scan.nextLine() + "\t" + "organism" +"\t" + "function"+"\t"+"ec");
            while(coFile_scan.hasNextLine()){
                String line = coFile_scan.nextLine();
		String[] parts = line.split("\t");
		String organism = "null";
		String function = "null";
		if(org.containsKey(parts[0])){
		    organism = org.get(parts[0]);
		}
		String ectemp = "";
		if(fun.containsKey(parts[0])){
			
		    ArrayList<String> functions = fun.get(parts[0]);
		    function = functions.get(0);
		    String[] ec = function.split("EC:");
		    if(ec.length > 1){
		    	ectemp = ec[1].split("\\)")[0];
		    	//System.out.println(ectemp);
		    }
		}
		String ecnum = "null";
		if(ectemp != ""){
			ecnum = ectemp;
		}
		Result.println(line + "\t" + organism +"\t" + function+"\t"+ecnum);
            }
	}catch (FileNotFoundException e){
            e.printStackTrace();
        }
	
    }
}