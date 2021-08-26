/**
 * Class for creating a peperback book with a title, author, price, and
 * a page count.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class Paperback {
    private static final double PRICE = 10;
    private Paperback( ) {
    }

    public static Book create( final Title title, final Author author, 
                           final double pageCount ) {
        return ConcreteBook.create( title, author, PRICE, pageCount, 
                                    ConcretePrintedBook.create( ) );
    }
}
