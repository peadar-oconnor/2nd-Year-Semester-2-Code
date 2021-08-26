/**
 * Class for representing an audiobook with a title, author, price and 
 * duration.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class ConcreteAudioBook implements BookType {
    private ConcreteAudioBook( ) { }

    public static BookType create( ) {
        return new ConcreteAudioBook( ) ;
    }

    @Override
    public String getFullString( final Title title, final Author author,
                final double price, final double length ) {
        final String fullString;
        fullString = "Title = " + title.getFullTitle( ) + ", Author = " +
            author.toString( ) + ", Price = " + price + ", Duration = " + length;
        return fullString;
    }
}

