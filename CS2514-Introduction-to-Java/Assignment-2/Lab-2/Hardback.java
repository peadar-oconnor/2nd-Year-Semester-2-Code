/**
 * Class for creating a hardback book with a title, author, price, and
 * a page count.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class Hardback {
    private static final double PRICE = 12;
    private Hardback( ) {
    }

    public static Book create( final Title title, final Author author,
                           final double pageCount ) {
        return ConcreteBook.create( title, author, PRICE, pageCount,
                                    ConcretePrintedBook.create( ) );
    }
}

