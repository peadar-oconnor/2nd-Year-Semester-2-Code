import java.util.ArrayList;

/**
 * Class for representing a reader who can buy books.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public class Reader implements Person {
    final Person p = new ConcretePerson( );
    final String firstName;
    final String lastName;

    public Reader(final String first, final String last) {
        this.firstName = first;
        this.lastName = last;
    }

    public String getName( ) {
        final String name = firstName + " " + lastName;
        return name;
    }
    
    @Override
    public double getEarnings( ) {
        return p.getEarnings( );
    }

    @Override
    public void buy( final Book book ) {
        p.buy( book );
    }

    @Override
    public void charge( final double money ) {
        p.charge( money );
    }   

    @Override
    public void receive( final double money ) {
        p.receive( money );
    }   

    @Override
    public void printArray( final ArrayList<Book> books ) {
        p.printArray( books );
    }

    @Override
    public void printBooksOwned( ) {
        final String whoOwns = this.getName() + " owns: ";
        System.out.println( whoOwns );
        p.printBooksOwned( );
    } 

    @Override
    public String toString( ) {
        return this.getName( );
    }
}
