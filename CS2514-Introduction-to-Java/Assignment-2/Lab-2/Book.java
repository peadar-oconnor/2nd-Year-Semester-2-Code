/**
 * Interface for providing methods to different books.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public interface Book extends BookType { 
    public String getTitle( );
    public double getPrice( );
    public Author getAuthor( );
}
