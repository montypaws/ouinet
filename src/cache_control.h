#pragma once

#include <boost/asio/error.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/asio/spawn.hpp>
#include <boost/beast/http.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>
#include "util/yield.h"
#include "cache/cache_entry.h"
#include "namespaces.h"

namespace ouinet {

class CacheControl {
public:
    using Request   = http::request<http::string_body>;
    using Response  = http::response<http::dynamic_body>;
    using TCPLookup = asio::ip::tcp::resolver::results_type;

    // TODO: Add cancellation support
    using FetchStored = std::function<CacheEntry(const Request&, Yield)>;
    using FetchFresh  = std::function<Response(const Request&, const TCPLookup&, Yield)>;
    // This function may alter a (moved) response and return it.
    using Store       = std::function<Response(const Request&, Response, Yield)>;

public:
    CacheControl(std::string server_name)
        : _server_name(std::move(server_name))
    {}

    Response fetch(const Request&, const TCPLookup&, Yield);

    FetchStored  fetch_stored;
    FetchFresh   fetch_fresh;
    Store        store;

    Response try_to_cache(const Request&, Response, Yield) const;

    void max_cached_age(const boost::posix_time::time_duration&);
    boost::posix_time::time_duration max_cached_age() const;

    // Returns ptime() if parsing fails.
    static boost::posix_time::ptime parse_date(beast::string_view);

    static bool ok_to_cache( const http::request_header<>&  request
                           , const http::response_header<>& response
                           , const char** reason = nullptr);

    // Keep only relevant headers and Ouinet internal headers,
    // (to be managed by the lower level functions above).
    static Response filter_before_store(Response);

private:
    // TODO: Add cancellation support
    Response do_fetch(const Request&, const TCPLookup&, Yield);
    Response do_fetch_fresh(const Request&, const TCPLookup&, Yield);
    CacheEntry do_fetch_stored(const Request&, Yield);

    bool is_stale( const boost::posix_time::ptime& time_stamp
                 , const Response&) const;

    bool is_older_than_max_cache_age(const boost::posix_time::ptime&) const;

    Response bad_gateway(const Request&, beast::string_view reason);

private:
    std::string _server_name;

    boost::posix_time::time_duration _max_cached_age
        = boost::posix_time::hours(7*24);  // one week
};

} // ouinet namespace
