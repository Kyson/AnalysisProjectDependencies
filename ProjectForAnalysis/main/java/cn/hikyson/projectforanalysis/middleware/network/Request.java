package cn.hikyson.projectforanalysis.middleware.network;


import cn.hikyson.projectforanalysis.base.log.Log;
import cn.hikyson.projectforanalysis.base.storage.DB;
import cn.hikyson.projectforanalysis.base.util.Util;

/**
 * Created by kysonchao on 2017/8/13.
 */
public class Request {
    private Log mLog = new Log();
    private DB mDB;

    private void ok() {
        Util.ok();
    }
}
