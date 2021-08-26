/**
 * Interface for encapsulating each different book type (audio/printed).
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public interface BookType {
    public String getFullString( final Title title, final Author author, 
                      final double price, final double length );
}
