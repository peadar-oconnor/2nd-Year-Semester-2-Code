/**
 * Class for representing book title which has a main title, and can 
 * have a sub-title.
 *
 * @author Peadar O'Connor (ID 117302273)
 */
public class Title {
    private final String mainTitle;
    private final String subTitle;
    private final String fullTitle;

    public Title( final String title ) {
        this.mainTitle = title;
        this.subTitle = "";
        this.fullTitle = title;
    }

    public Title( final String main, final String sub ) {
        this.mainTitle = main;
        this.subTitle = sub;
        this.fullTitle = main + " / " + sub;
    }

    public String getFullTitle( ) {
        return fullTitle; 
    }

    @Override
    public String toString( ) {
        return getFullTitle( );
    }
        
}
