/**
 * Class for representing a book with a title, author, price, length and
 * type of book.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public final class ConcreteBook implements Book {
    private final Title title;
    private final Author author;
    private final double price;
    private final double length;
    private BookType bookType;

    private ConcreteBook( final Title title, final Author author, 
                final double price, final double length,
                final BookType bookType) {
        this.title = title;
        this.author = author;
        this.price = price;
        this.length = length;
        this.bookType = bookType;
    }

    public static Book create( final Title title, final Author author,
                final double price, final double length,
                final BookType bookType ) {
        final Book book =  new ConcreteBook( title, author,
                                              price, length, bookType );
        author.publishBook( book );
        return book;
    }

    @Override
    public String getTitle( ) {
        return title.toString( );
    }
    
    @Override
    public double getPrice( ) {
        return price;
    }

    @Override
    public Author getAuthor( ) {
        return author;
    }

    @Override
    public String getFullString( final Title title, final Author author,
                final double price, final double length ) {
        final String fullString;
        fullString = bookType.getFullString( title, author,
                         price, length );
        return fullString;
    }

    @Override
    public String toString( ) {
        return this.getFullString( title, author, price, length );
    }

}
