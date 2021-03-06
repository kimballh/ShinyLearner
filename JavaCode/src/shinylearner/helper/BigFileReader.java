package shinylearner.helper;

import shinylearner.core.Log;

import java.io.*;
import java.util.Iterator;
import java.util.zip.GZIPInputStream;

/** This helper class is designed to aid in the process of parsing (potentially large) text files. It stores little data in memory, thus making it possible to parse very large files.
 * @author Stephen Piccolo
 */
public class BigFileReader implements Iterable<String>
{
    private BufferedReader _reader;

    /** Constructor
     *
     * @param filePath Absolute file path of file to be read
     * @throws Exception
     */
    public BigFileReader(String filePath) throws Exception
    {
    	if (filePath.endsWith(".gz"))
    	{
	    	InputStream fileStream = new FileInputStream(filePath);
	    	InputStream gzipStream = new GZIPInputStream(fileStream);
	    	Reader decoder = new InputStreamReader(gzipStream);
	    	_reader = new BufferedReader(decoder);
    	}
    	else
    	{
    		_reader = new BufferedReader(new FileReader(filePath));
    	}
    }

    /** Closes the file connection. */
    public void Close()
    {
        try
        {
            _reader.close();
        }
        catch (Exception ex)
        {
            Log.ExceptionFatal(ex);
        }
    }

    public Iterator<String> iterator()
    {
        return new BigFileIterator();
    }

    /** Reads a single line of the file
     *
     * @return Text of line
     * @throws Exception
     */
    public String ReadLine() throws Exception
    {
        return _reader.readLine();
    }

    /** This class iterates over the lines of a (potentially big) file
     * @author Stephen Piccolo
     */
    public class BigFileIterator implements Iterator<String>
    {
        private String _currentLine;
        private int _count = 0;

        public boolean hasNext()
        {
            try
            {
                _currentLine = _reader.readLine();
            }
            catch (Exception ex)
            {
                _currentLine = null;
                Log.ExceptionFatal(ex);
            }

            if (_currentLine == null)
            {
                try
                {
                    Close();
                }
                catch (Exception ex)
                {
                    Log.ExceptionFatal(ex);
                }
                return false;
            }
            else
                return true;
        }

        public String next()
        {
            _count++;

            if (_count % 10000 == 0)
                Log.Debug("Lines read: " + _count);

            return _currentLine.trim();
        }

        public void remove()
        {
        }
    }
}
