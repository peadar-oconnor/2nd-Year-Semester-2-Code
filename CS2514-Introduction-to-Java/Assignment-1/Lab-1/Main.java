import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main( final String[] args ) {
        final List<Garment> items = new ArrayList<Garment>( );
        final Jeans jeans = new Jeans( );
        final Tshirt tshirt = new Tshirt( );
        final WinterCoat winterCoat = new WinterCoat( );
        final RainCoat rainCoat = new RainCoat( );
        final Jacket jacket = new Jacket( ); 
        items.add( jeans );
        items.add( tshirt );
        items.add( winterCoat );
        items.add( rainCoat );
        items.add( jacket );

        for (Garment item : items) {
            item.printPurpose( );
        }

        System.out.println( );

        for (Garment item : items) {
            item.printItemisedBill( );
        }
    }
}
