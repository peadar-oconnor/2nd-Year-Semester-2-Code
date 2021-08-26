/**
 * Main class for demonstrating my constructor and method calls.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public class Main {
    public static void main( final String[] args ) {
        final Title t1 = new Title( "The Hobbit", "An Unexpected Journey" );
        final Title t2 = new Title( "Catcher in the Rye" );
        final Title t3 = new Title( "Murder on the Orient Express" );
        final Author a1 = Author.JRR_Tolkien;
        final Author a2 = Author.JD_Sallinger;
        final Author a3 = Author.Agatha_Christie;
        final Author a4 = Author.Stephen_King;
        final Book b1 = AudioBook.create( t1, a1, 1800.5 );
        final Book b2 = Paperback.create( t2, a2, 100 );
        final Book b3 = Hardback.create( t3, a3, 345 );
        final Reader r1 = new Reader( "Joe", "Soap" );
        
        a1.receive( 100 );
        a1.buy( b2 );
        r1.buy( b1 );
        r1.printBooksOwned( );
        r1.receive( 100 );
        r1.buy( b1 );
        r1.buy( b2 );
        a1.printBooksOwned( );
        a1.printBooksPublished( );
        r1.printBooksOwned( );
        // a1 owns 100 - 10 + 0.10 * 15 = 91.5 Euro
        System.out.println( a1 + " owns " + a1.getEarnings( ) + " Euro" );
        r1.buy( b3 );
        r1.printBooksOwned( );
        // r1 owns 100 - (15+12+10) = 63.0 Euro
        System.out.println( r1 + " owns " + r1.getEarnings( ) + " Euro" );
        a3.printBooksOwned( );
        a3.printBooksPublished( );
        a4.printBooksOwned( );
        a4.printBooksPublished( );
    }
}
