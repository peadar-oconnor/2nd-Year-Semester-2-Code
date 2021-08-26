/**
 * Class for creating an audiobook with a title, author, price and 
 * duration.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class AudioBook {
    private static final double PRICE = 15;
    private AudioBook( ) {
    }

    public static Book create( final Title title, final Author author,
                           final double duration ) {
        return ConcreteBook.create( title, author, PRICE, duration,
                                    ConcreteAudioBook.create( ) );
    }
}

