/**
 * Class for representing a printed book with a title, author, price, 
 * and length.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class ConcretePrintedBook implements BookType {
    private ConcretePrintedBook( ) { }

    public static BookType create( ) {
        return new ConcretePrintedBook( ) ;
    }

    @Override
    public String getFullString( final Title title, final Author author,
                final double price, final double length ) {
        final String fullString;
        final String roundedLength = String.format("%.0f", length);
        fullString = "Title = " + title.getFullTitle( ) + ", Author = " + 
            author.toString( ) + ", Price = " + price + 
            ", Page Count = " + roundedLength;
        return fullString;
    }
}
