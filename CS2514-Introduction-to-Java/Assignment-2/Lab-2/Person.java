import java.util.ArrayList;

/**
 * Interface for providing methods to the person class.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public interface Person {
    public double getEarnings( );
    public void buy( final Book book );
    public void charge( final double money );
    public void receive( final double money );
    public void printArray( final ArrayList<Book> books );
    public void printBooksOwned( );
}
