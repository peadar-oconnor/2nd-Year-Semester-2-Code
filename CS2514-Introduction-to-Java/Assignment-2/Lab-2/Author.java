import java.util.ArrayList;

/**
 * Class for representing an Author who can buy and publish books.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public enum Author implements Person {
    JRR_Tolkien ("J.R.R. Tolkien"),
    JD_Sallinger ("J.D. Sallinger"),
    Agatha_Christie ("Agatha Christie"),
    Stephen_King ("Stephen King");
    final Person p = new ConcretePerson( );
    final String name;
    final ArrayList<Book> booksPublished;

    private Author( final String name ) {
        this.name = name;
        this.booksPublished = new ArrayList<Book>( );
    }

    public String getName( ) {
        return name;
    }

    public void publishBook( final Book book ) {
        booksPublished.add( book );
    }

    public void printBooksPublished( ) {
        final String whoPublished = this.getName() + " published: ";
        System.out.println( whoPublished );
        p.printArray( booksPublished );
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
        return name;
    }
}
