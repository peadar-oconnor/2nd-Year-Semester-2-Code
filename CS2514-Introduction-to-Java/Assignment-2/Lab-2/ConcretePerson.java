import java.util.ArrayList;

/**
 * Class for representing a person who can buy books.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public class ConcretePerson implements Person {
    private ArrayList<Book> booksOwned;
    private double earnings;

    public ConcretePerson( ) {
        this.booksOwned = new ArrayList<Book>( );
        this.earnings = 0.0;
    }

    public ArrayList<Book> getBooksOwned( ) {
        return booksOwned;
    }

    @Override
    public double getEarnings( ) {
        return earnings;
    }

    @Override
    public void buy( final Book book ) {
        if (book.getPrice( ) > earnings) {
            final String error = "You don't have enough money to buy\n    " + 
                                 book;
            System.out.println(error);
        } else {
            booksOwned.add( book );
            this.charge( book.getPrice( ) );
            final double authorsCut = book.getPrice( ) * 0.1;
            // code to add authors_cut to authors earnings
            final Author a = book.getAuthor( );
            a.receive( authorsCut );
        }
    }

    @Override
    public void charge( final double money ) {
        earnings = earnings - money;
    }

    @Override
    public void receive( final double money ) {
        earnings = earnings + money;
    }

    @Override
    public void printArray( final ArrayList<Book> books ) {
        if ( books.size( ) > 0 ) {
            for ( Book book : books ) {
                System.out.println("    " + book.getTitle( ).toString( ));
            } 
        } else {
            System.out.println("    No Books.");
        }
    }

    @Override
    public void printBooksOwned( ) {
        this.printArray( booksOwned );
    }
}






