public interface A{
    public void render{}
} 
public interface B extends A{
}   
public class C implements A {
    public void render(){
        System.out.println("C's render");
    }

}